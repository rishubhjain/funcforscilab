function[img_ret]=cv_thresh_binary(image)
    pyImport simple_thresholding
    img_ret=simple_thresholding.thresh_binary(image)
endfunction