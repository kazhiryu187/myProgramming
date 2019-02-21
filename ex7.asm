global _start

_start:
    call func
    mov eax, 1
    int 80h
    
func:
   mov ebx, 42
   ;pop eax
   ;jmp eax
   ret
