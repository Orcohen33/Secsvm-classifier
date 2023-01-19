# -*- coding: utf-8 -*-

"""
settings.py
~~~~~~~~~~~

Configuration options for the pipeline.

"""
import os

# The absolute path to the root folder of this project
_project_path = '/home/or/Desktop/secsvm/'
# The absolute path of the folder containing compiled Java components
_components_path = '/home/or/Desktop/secsvm/java-components/build'

fromer_dataset="/home/harel/intriguing-2020/data_for_secsvm/former_malicious_test/0/"
datasets_for_secsvm="/home/or/Desktop/secsvm/data_for_niv_avi/train/"
COM_dataset="/home/or/Desktop/secsvm/data_for_niv_avi/test/"
SB_dataset="/home/or/Desktop/secsvm/data_for_niv_avi/test/"
MB1_dataset="/home/or/Desktop/secsvm/data_for_niv_avi/test/"
MB2_dataset="/home/or/Desktop/secsvm/data_for_niv_avi/test"
MB3_dataset="/home/or/Desktop/secsvm/data_for_niv_avi/test"
MB4_dataset="/home/or/Desktop/secsvm/data_for_niv_avi/test/"
def _project(base):
    return os.path.join(_project_path, base)


def _components(base):
    return os.path.join(_components_path, base)


config = {
    # Experiment settings
    'models': _project('data/models/'),
    'X_dataset': _project(datasets_for_secsvm+'train_dataset.json'),
    'y_dataset': _project(datasets_for_secsvm+'labels.json'),
    'X_dataset_test': _project(MB4_dataset+'test_dataset.json'),
    'y_dataset_test': _project(MB4_dataset+'labels.json'),
    'meta': _project('data/features/labels.json'),
    'indices': _project(''),  # only needed if using fixed indices
    # Java components
    'extractor': _components('extractor.jar'),
    'injector': _components('injector.jar'),
    'template_injector': _components('templateinjector.jar'),
    'cc_calculator': _components('cccalculator.jar'),
    'class_lister': _components('classlister.jar'),
    'classes_file': _project('all_classes.txt'),
    'extractor_timeout': 300,
    'cc_calculator_timeout': 600,
    # Other necessary components
    'android_sdk': '/usr/lib/android-sdk',
    'template_path': _project('template'),
    'mined_slices': _project('mined-slices'),
    'opaque_pred': _project('opaque-preds/sootOutput'),
    'resigner': _project('apk-signer.jar'),
    'feature_extractor': '/home/or/Desktop/secsvm/feature-extractor',
    # Storage for generated bits-and-bobs
    'tmp_dir': '/home/or/Desktop/secsvm/tmp',
    'ice_box': '/home/or/Desktop/secsvm/ice_box',
    'results_dir': '/home/or/Desktop/secsvm/res',
    'goodware_location': '/home/or/Desktop/secsvm/res',
    'storage_radix': 0,  # Use if apps are stored with a radix (e.g., radix 3: root/0/0/A/00A384545.apk)
    # Miscellaneous options
    'tries': 1,
    'nprocs_preload': 8,
    'nprocs_evasion': 12,
    'nprocs_transplant': 8
}
