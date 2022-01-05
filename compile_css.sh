#! /bin/zsh

sass --load-path=scss --watch scss/base:app/base/static \
    scss/students:app/students/static \
    scss/auth:app/util/static \
    scss/career_services:app/career_services/static