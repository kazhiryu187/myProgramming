global _start
_start:
    sub esp, 4
    mov [esp],   byte 'G'
    mov [esp+1], byte 'W'
    mov [esp+2], byte 'A'
    mov [esp+3], byte 'R'
    mov eax, 4  ; system call number (sys_write)
    mov ebx, 1  ; file descriptor (stdout)
    mov ecx, esp  ; pointer to bytes to write
    mov edx, 4   ; number of bytes to write
    int 0x80    ; call kernal
    mov eax, 1  ; system call number (sys_exit)
    mov ebx, 0  ; exit status is 0
    int 0x80
