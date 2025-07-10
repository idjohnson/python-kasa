
from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def run_kasa_command(command: list[str]):
    try:
        process = subprocess.run(
            ["/usr/local/bin/kasa"] + command,
            capture_output=True,
            text=True,
            check=True,
        )
        return process.stdout
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Kasa command failed: {e.stderr}")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/on")
def turn_on(devip: str, type: str = "plug"):
    return {"output": run_kasa_command(["--host", devip, "--type", type, "on"])}

@app.post("/off")
def turn_off(devip: str, type: str = "plug"):
    return {"output": run_kasa_command(["--host", devip, "--type", type, "off"])}

@app.post("/swap")
def swap(devip: str, type: str = "plug"):
    state_output = run_kasa_command(["--host", devip, "--type", type, "state"])
    if "Device state: OFF" in state_output:
        return {"output": run_kasa_command(["--host", devip, "--type", type, "on"])}
    else:
        return {"output": run_kasa_command(["--host", devip, "--type", type, "off"])}
