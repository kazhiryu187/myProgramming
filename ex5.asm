global _start

section .data
   addr db "yellow"

section .text
_start:
   mov [addr], byte 'H'
   mov [addr+5], byte '!'
   mov eax, 4      ; system call number (sys_write)
   mov ebx, 1      ; file descriptor (stdout)
   mov ecx, addr   ; bytes to write
   mov edx, 6      ; number of bytes to write
   int 0x80        ; call kernel
   mov eax, 1      ; system call number (sys_exit)
   mov ebx, 0
   int 0x80
