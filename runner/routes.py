import os

from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/")
async def index(req: web.Request) -> web.Response:
    return web.Response(body=f"run-runner {os.environ['GIT_COMMIT']}")


@routes.route("OPTIONS", "/health_check")
async def healthcheck(req: web.Request) -> web.Response:
    return web.Response(status=200)


@routes.post("/run")
async def run_code(req: web.Request) -> web.Response:
    return web.json_response(
        dict(stdout="Code execution successfull\n", stderr="", exit_code=0, exec_time=1)
    )
