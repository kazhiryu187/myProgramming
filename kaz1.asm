global _start

_start:
    mov eax, 1
    mov ebx, 53
    mov ecx, 3
    add ebx, ecx
    int 0x80
    
