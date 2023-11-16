import uvicorn


def run_app():
    app_dir = "app.app"

    uvicorn.run(
        f"{app_dir}:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    run_app()
