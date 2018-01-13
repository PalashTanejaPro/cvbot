set -e -x

docker build -t meetmangukiya/cvbot .
.ci/semaphore.answers.sh

docker images

docker run --user root meetmangukiya/cvbot /bin/sh -c "
    set -e -x
    pip install -r test-requirements.txt
    find -name \"**.pyc\" -delete
    python -m pytest
"

if [[ $BRANCH_NAME == "master" ]]
then echo "pushing..." && docker push meetmangukiya/cvbot && docker push meetmangukiya/cvbot-answers
fi
