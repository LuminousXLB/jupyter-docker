FROM jupyter/scipy-notebook

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

COPY condarc /opt/conda/.condarc
COPY npmrc /home/$NB_USER/.npmrc

RUN pip3 config set global.index-url https://mirrors.sjtug.sjtu.edu.cn/pypi/web/simple \
    && pip3 install --no-cache-dir \
    jupyterlab-lsp \
    jupyterlab_code_formatter \
    xlsxwriter \
    requests \
    httpx \
    lxml \
    html5lib \
    black \
    isort \
    && jupyter serverextension enable --py jupyterlab_code_formatter \
    && jupyter labextension install @ryantam626/jupyterlab_code_formatter --no-build \
    && jupyter labextension install '@krassowski/jupyterlab-lsp@2.1.2' --no-build \
    && jupyter lab build --minimize=False -y \
    && jupyter lab clean -y \
    && mkdir -p /home/$NB_USER/.cache/black/20.8b1 \
    && npm cache clean --force \
    && rm -rf "/home/${NB_USER}/.cache/yarn" \
    && rm -rf "/home/${NB_USER}/.node-gyp" \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

COPY pycodestyle /home/$NB_USER/.config/pycodestyle
COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/jupyter_notebook_config.py
COPY fonts/*.otf /home/$NB_USER/.fonts/

RUN fc-cache && \
    python -c "from matplotlib import font_manager; font_manager._rebuild()"
# && \
# pip3 uninstall -y jedi && \
# pip3 install --no-cache-dir \
# 'jedi<0.18.0,>=0.17.2'

USER $NB_UID

WORKDIR $HOME/work
