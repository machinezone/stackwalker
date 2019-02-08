# Used for easy compilation testing on Linux from a mac.

all: docker run

#
# Docker
#
NAME   := stackwalker
TAG    := $(shell cat VERSION)
IMG    := ${NAME}:${TAG}
LATEST := ${NAME}:latest
BUILD  := ${NAME}:build
PROD   := ${NAME}:production

docker:
	docker build -t ${IMG} .
	docker tag ${IMG} ${BUILD}
	docker tag ${IMG} ${PROD}

run:
	docker run -it ${BUILD} sh
