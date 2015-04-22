function [image] = cv_rgb2gray_path(path)  
    
    pyImport rgb2gray_file
    image=rgb2gray_file.rgb2gray(path)
    
    
endfunction 
