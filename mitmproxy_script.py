from mitmproxy import http, ctx


def request(flow: http.HTTPFlow) -> None:
    # 输出请求信息
    ctx.log.info(f"Request URL: {flow.request.pretty_url}")
    ctx.log.info(f"Request Method: {flow.request.method}")
    ctx.log.info(f"Request Headers: {flow.request.headers}")
    ctx.log.info(f"Request Content: {flow.request.content}")


def response(flow: http.HTTPFlow) -> None:
    # 输出响应信息
    ctx.log.info(f"Response Status Code: {flow.response.status_code}")
    ctx.log.info(f"Response Headers: {flow.response.headers}")
    ctx.log.info(f"Response Content: {flow.response.content}")

# 启动 mitmproxy
# mitmproxy -s mitmproxy_script.py
