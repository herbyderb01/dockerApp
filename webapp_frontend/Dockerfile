# Use an official node image as our base image
FROM node:current-slim

# Set the working directory to /contacts_app
WORKDIR ${WORKDIR_FRONTEND}

# Make back end of this container available to the world outside this container
EXPOSE ${BACKEND_PORT}

# Which mode are we working in
ENV NODE_ENV=development
# ENV NODE_ENV=production

COPY ./package.json ./
COPY ./yarn.lock ./

# Install npm (dev or production)
RUN npm install
# RUN yarn install
# RUN npm install --production --silent && mv node_modules ../

# Copy in the rest of the files from webapp_frontend to WORKDIR_FRONTEND
# COPY ./webapp_frontend .
COPY . .

# RUN chown -R node /usr/app/contacts_app
# USER node

CMD ["npm", "start"]
# RUN npm start -- --port ${BACKEND_PORT}