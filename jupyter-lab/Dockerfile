FROM jupyter/scipy-notebook

COPY condarc $CONDA_DIR/.condarc
COPY npmrc $HOME/.npmrc
COPY pycodestyle $HOME/.config/pycodestyle
COPY jupyter_notebook_config.py $HOME/.jupyter/jupyter_notebook_config.py

COPY fonts/*.otf $HOME/.fonts/

RUN pip3 config set global.index-url https://mirrors.sjtug.sjtu.edu.cn/pypi/web/simple \
    && pip3 install --no-cache-dir \
    jupyterlab-lsp \
    'python-lsp-server[all]' \
    jupyterlab_code_formatter \
    black \
    html5lib \
    httpx \
    isort \
    lxml \
    xlsxwriter \
    && jupyter serverextension enable --py jupyterlab_code_formatter \
    && jupyter labextension install @ryantam626/jupyterlab_code_formatter --no-build \
    && jupyter labextension install '@krassowski/jupyterlab-lsp@2.1.2' --no-build \
    && jupyter lab build --minimize=False -y \
    && jupyter lab clean -y \
    && npm cache clean --force \
    && rm -rf "/home/${NB_USER}/.cache/yarn" \
    && rm -rf "/home/${NB_USER}/.node-gyp" \
    && fix-permissions $HOME \
    && fix-permissions $CONDA_DIR \
    && fc-cache

USER $NB_UID

WORKDIR $HOME/work
