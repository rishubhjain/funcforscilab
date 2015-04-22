function[image_ret]=cv_Line(image,start,end1,color1)
    pyImport drawing_file
    //omitted parameters like thickness, lineType, shift
    image_ret=drawing_file.myLine(image,start,end1,color1)
endfunction