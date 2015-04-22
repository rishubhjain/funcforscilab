
function [img_ret]=cv_equalizeHist_path(path)
    pyImport equalizeHist_file
    img_ret=equalizeHist_file.equalizeHist_path(path)
endfunction
