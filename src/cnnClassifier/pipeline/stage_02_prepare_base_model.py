from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME="Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_base_model_confg=config.get_prepare_base_model_config()
        prepare_base_model=PrepareBaseModel(prepare_base_model_confg)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info("********************")
        logger.info(f">>>>>>>>>>s stege {STAGE_NAME} started <<<<<<<<<<")
        obj=PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n==========x")
    except Exception as e:
        logger.exception(e)
        raise e