TOOLS = ["requirements", "architecture", "terraform_generate", "security_validate"]
WRITES = ("terraform apply", "gcloud deploy", "destroy",)

def run(goal, payload):
    if not goal or not str(goal).strip():
        raise ValueError("goal is empty")
    low = goal.lower()
    if any(w in low for w in WRITES):
        return {"refused": True, "reason": "destructive action requires a human", "applied": False, "tools": []}
    result = {"ha": True, "db": "postgresql", "dr": "regional", "modules": ["vpc", "gke", "cloudsql"]}
    return {"refused": False, "tools": TOOLS, "proposal": result, "applied": False, "needs_approval": False}
