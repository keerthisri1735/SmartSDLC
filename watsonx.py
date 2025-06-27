import os
from ibm_watsonx_ai.foundation_models import ModelInference
from dotenv import load_dotenv

load_dotenv()

def watsonx_client():
    return ModelInference(
        model_id="ibm/granite-20b-multilingual",
        project_id=os.getenv("IBM_PROJECT_ID"),
        credentials={"apikey": os.getenv("IBM_API_KEY")},
        deployment_id=os.getenv("IBM_DEPLOYMENT_ID")
    )

def classify_sdlc(sentences):
    client = watsonx_client()
    prompt = """
    Classify each of the following sentences into one of the SDLC phases:
    Requirements, Design, Development, Testing, or Deployment.

    Sentences:
    {lines}
    """.format(lines="\n".join(sentences))
    response = client.generate_text({"input": prompt})
    return response.get("generated_text", "No output")