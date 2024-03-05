#! /bin/sh
# shellcheck disable=SC2086

set -x
set -e
root_dir=$(cd $(dirname $0); pwd)
cd $root_dir

labbooks=$(ls $root_dir/assignments)
echo "Found labbooks: ${labbooks}"
for lb in $labbooks
do
  cd $root_dir
  labbook_dir=assignments/$lb
  if [ -d $labbook_dir ]
  then
      echo "Building $lb"
      labbook_fn=labbook$lb.tex
      cd $labbook_dir
      if [ ! -f $labbook_fn ]
      then
        echo "::error::Directory 'assignments/$lb' is expected to contain a file called '$labbook_fn', but it is not there. Please check that you haven't renamed or moved things that aren't supposed to be moved or renamed" >&2
        exit 1
      fi

      test -d build || mkdir build
      
      echo "::group::Compiling $lb"
      set +e
      pdflatex -halt-on-error -output-directory build $labbook_fn
      latex_exit=$?
      set -e
      echo "::endgroup::"
      if [ $latex_exit = 0 ]
      then
        echo "::notice::Labbook $lb compiled successfully"
      else
        echo "::error::Labbook $lb failed to compile!"
        exit 1
      fi
  fi
done
echo "::notice::Everything compiles, commit hash: $(git rev-parse HEAD) $lb compiled successfully"
