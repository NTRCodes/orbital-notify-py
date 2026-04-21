from app import create_app

app = create_app()

# Only run with `uvicorn app.main:create_app` in dev mode
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:create_app", reload=True)