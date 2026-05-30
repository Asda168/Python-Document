i = 2
j = 10

for y in range(i, j): # y = 2, 3, 4, 5, 6, 7, 8, 9

    for x in range(i, y): # x goes from 2 up to (y-1)
        if y % x == 0:
            print(f"{y} equals {x} * {int(y/x)}")
            break
    else:
        print(f"{y} is a prime number")


#   Data processing

# High Address  ┌─────────────────┐
#               │      Stack      │  ← Function calls, local variables
#               │        ↓        │
#               │   (grows down)  │
#               │                 │
#               │   (grows up)    │
#               │        ↑        │
#               │      Heap       │  ← Dynamic memory (malloc, new)
#               ├─────────────────┤
#               │      Data       │  ← Global & static variables
#               ├─────────────────┤
# Low Address   │      Code       │  ← Program instructions (text)
#               └─────────────────┘


# Process States

# ┌──────────────────────────────────────────┐
#          │                                          │
#          ▼                                          │
#        NEW  ──── admitted ────►  READY  ◄─── I/O complete
#                                   │
#                          dispatcher│
#                                   ▼
#                               RUNNING  ──── exit ────► TERMINATED
#                                   │
#                           I/O or event│
#                                   ▼
#                               WAITING


# Process Control Block (PCB)

# ┌──────────────────────┐
# │   Process ID (PID)   │  ← Unique identifier
# ├──────────────────────┤
# │    Process State     │  ← Running, Ready, Waiting...
# ├──────────────────────┤
# │   Program Counter    │  ← Next instruction to execute
# ├──────────────────────┤
# │  CPU Registers       │  ← Current register values
# ├──────────────────────┤
# │  Memory Information  │  ← Base/limit, page tables
# ├──────────────────────┤
# │   I/O Information    │  ← Open files, devices
# ├──────────────────────┤
# │  Scheduling Info     │  ← Priority, queue pointers
# └──────────────────────┘

# ------------------------------
# Process Life Cycle
# ------------------------------

# NEW → READY → RUNNING → WAITING → TERMINATED