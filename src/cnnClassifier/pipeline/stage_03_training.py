
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.training import Training
from cnnClassifier import logger


STAGE_NAME="Model Training"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_callback_config=config.get_prepare_callback_config()
        prepare_callbacks=PrepareCallback(prepare_callback_config)
        callback_list=prepare_callbacks.get_tb_ckpt_callbacks()

        training_config=config.get_training_config()
        training=Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


if __name__=="__main__":
    try:
        logger.info("********************")
        logger.info(f">>>>>>>>>> state  {STAGE_NAME} started <<<<<<<<<<")
        obj=TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> state  {STAGE_NAME} completed <<<<<<<<<<\n\n")
    except Exception as e:
        raise e


