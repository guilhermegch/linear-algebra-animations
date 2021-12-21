clear;
clc;

I = imread("Imagens/windowsxp.redimensionado.jpg");

% Função que decompoe e comprime a foto
% A = matrix de entrada, N = numero de valores singulares a serem mantidos
function [Uc, Sigmac, Vc] = compress_matrix(A, N)
    [U, Sigma, V] = svd(A);
    Uc = U(:, 1:N);
    Sigmac = Sigma(1:N, 1:N);
    Vc = V(:, 1:N);
end


% Rodar apenas uma vez
N = 50;
 
[U1c, Sigma1c, V1c] = compress_matrix(I(:,:,1), N);
[U2c, Sigma2c, V2c] = compress_matrix(I(:,:,2), N);
[U3c, Sigma3c, V3c] = compress_matrix(I(:,:,3), N);
 
Ic = uint8( zeros(size(I,1), size(I,2), 3) );
 
Ic(:,:,1) = uint8(U1c * Sigma1c * V1c');
Ic(:,:,2) = uint8(U2c * Sigma2c * V2c');
Ic(:,:,3) = uint8(U3c * Sigma3c * V3c');

imshow(Ic)


% Rodar várias vezes
%{
for N = [500, 250, 100, 050, 025, 015, 010, 005, 001]
    [U1c, Sigma1c, V1c] = compress_matrix(I(:,:,1), N);
    [U2c, Sigma2c, V2c] = compress_matrix(I(:,:,2), N);
    [U3c, Sigma3c, V3c] = compress_matrix(I(:,:,3), N);
    Ic = uint8( zeros(size(I,1), size(I,2), 3) );
    Ic(:,:,1) = uint8(U1c * Sigma1c * V1c');
    Ic(:,:,2) = uint8(U2c * Sigma2c * V2c');
    Ic(:,:,3) = uint8(U3c * Sigma3c * V3c');
    numero = sprintf('%03d', N);
    caminho_salvar = horzcat("Imagens/Saida/windowsxp_colorido-", numero, ".jpg");
    imwrite(Ic, caminho_salvar, 'Quality', 100)
 endfor
%}