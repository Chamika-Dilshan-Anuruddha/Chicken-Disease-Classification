from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    raise e


STAGE_NAME="Prepare Base Model"

try:
    logger.info("********************")
    logger.info(f">>>>>>>>>>s stege {STAGE_NAME} started <<<<<<<<<<")
    obj=PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n==========x")
except Exception as e:
    logger.exception(e)
    raise e