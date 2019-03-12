import zipfile
import uuid
import os
from cvpm.solver import Solver
from pystitch.pystitch import warmUp
from pystitch.process import automatic

class ImageStitchSolver(Solver):
    def __init__(self, toml_file=None):
        super().__init__(toml_file)
        warmUp()
        self.set_ready()

    def infer(self, image_file, config):
        # Extract files to project specific folder
        # TODO: This feature may be added to cvpm kernel
        zip_ref = zipfile.ZipFile(image_file)
        project_id = str(uuid.uuid4()).split('-')[0]
        project_folder = os.path.join('.','project', project_id)
        zip_ref.extractall(project_folder)
        zip_ref.close()
        ## Workflow
        automatic(project_folder, config['suffix'], project_id + '.pto')
        