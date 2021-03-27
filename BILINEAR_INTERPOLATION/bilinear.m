I = imread('baby_x2_GT.png');
Y = imresize(I,[160,256],'Method','lanczos3');
figure;
imshow(Y);