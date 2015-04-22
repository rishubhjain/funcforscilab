
function[image_ret]=cv_Rect(image,start,end1,color1)
    pyImport drawing_file
    image_ret=drawing_file.myRect(image,start,end1,color1)
endfunction