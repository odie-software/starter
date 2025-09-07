import { createProxyEventHandler } from "h3-proxy"

export default defineEventHandler(
  createProxyEventHandler({
    target: useRuntimeConfig().public.apiUrl,
    changeOrigin: true,
    pathRewrite: {
      "^/api": "",
    },
    pathFilter: ["/api"],
  }),
)
