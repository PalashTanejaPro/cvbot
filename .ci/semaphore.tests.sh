set -e -x

pip install cloudcv-bears
pip install -r requirements.txt
pip install -r test-requirements.txt
sed -i.bak '/bears = GitCommitBear/d' .coafile
cloudcv --ci -V
python -m pytest
codecov
