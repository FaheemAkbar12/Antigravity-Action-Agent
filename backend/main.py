from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from workflow_engine import AntigravityWorkflowEngine

app = FastAPI(title="Google Antigravity Autonomous Insight-to-Action System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = AntigravityWorkflowEngine()


class ReportRequest(BaseModel):
    content: str


@app.get("/")
def home():
    return {
        "status": "running",
        "platform": "Google Antigravity",
        "workflow_engine": "active"
    }


@app.post("/analyze")
def analyze(request: ReportRequest):
    return engine.orchestrate(request.content)


@app.get("/workflow-trace")
def workflow_trace():
    return engine.runtime.logs


@app.get("/system-state")
def system_state():
    return engine.runtime.state_manager.get_state()
