function[image_ret]=cv_Ellipse(img,cent, axes1, angle, startAngle, endAngle,color1)
    pyImport drawing_file
    image_ret=drawing_file.myLine(img,cent, axes1, angle, startAngle, endAngle,color1)
endfunction