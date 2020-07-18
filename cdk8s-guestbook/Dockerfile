FROM argoproj/argocd:latest

USER root

RUN apt-get update && \
    apt-get install -y \
        curl \
        python3-pip \
        python3-venv && \
    apt-get clean && \
    pip3 install pipenv constructs==2.0.2 cdk8s==0.26.0

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn && yarn global add npm cdk8s-cli

USER argocd
