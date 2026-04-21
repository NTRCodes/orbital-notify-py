from app import create_app


# Only run with `uvicorn app.main:create_app` in dev mode
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:create_app", factory=True, reload=True)