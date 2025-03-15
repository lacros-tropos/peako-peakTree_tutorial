import pypeako
import glob

cropped_files = glob.glob('PEAKO_files/24*cropped*.NC')

TD = pypeako.TrainingData(cropped_files,
                     num_spec=[10])
TD.mark_random_spectra()
TD.save_training_data()
