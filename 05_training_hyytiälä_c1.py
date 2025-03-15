import pypeako
import json
import glob
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cProfile
import copy
matplotlib.use('Agg')
# thorough training via both methods and testing

training_files_hyytiala = glob.glob('PEAKO spectra files/'
                                    'marked_peaks_*_cropped_*.LV0.NC')
print(training_files_hyytiala)

P = pypeako.Peako(
              training_files_hyytiala, plot_dir='plots/chirp_0/',
    k=0,
    training_params={'t_avg': [0], 'h_avg': [0], 'span': np.arange(0.05, 0.45, 0.05), 'polyorder':[2,3],
             'width': np.arange(0., 1, 0.5), 'prom': np.arange(0, 2.5, 0.5)},
    save_similarities=True,
   verbosity=10, temporary_files_flag=True,
     )

P.mask_chirps([1, 2])



P.create_training_mask()
print('number of marked spectra in this chirp:', P.get_training_sample_number())

print('training peako')
result = P.train_peako()
samples = [np.sum(P.marked_peaks_index[P.current_k][f].values == 1)
                       for f in range(len(P.spec_data))]


P.training_stats(make_3d_plots=True, k=0)

with open(f'{P.plot_dir}result_chirp1.txt', 'w+') as f:
    json.dump(result, f)

# plotting four example spectra with user-marked and PEAKO peaks:
P.plot_user_algorithm_spectrum(plot_smoothed=True)
P.plot_user_algorithm_spectrum(plot_smoothed=True)
P.plot_user_algorithm_spectrum(plot_smoothed=True)
P.plot_user_algorithm_spectrum(plot_smoothed=True)

