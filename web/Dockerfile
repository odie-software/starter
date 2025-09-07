# Dockerfile for Production

FROM node:22 AS build

WORKDIR /app
RUN npm install -g pnpm
COPY --link package.json pnpm-lock.yaml ./
RUN pnpm install
COPY --link . .
RUN pnpm build

FROM node:22-slim AS production

# Set environment variables for production
ENV NODE_ENV=production
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

WORKDIR /app

COPY --from=build /app/.output ./.output

# Expose the port the application will run on
EXPOSE 3000

# The command to start the Nuxt server in production
CMD [ "node", ".output/server/index.mjs" ]
