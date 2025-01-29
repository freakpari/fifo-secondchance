def second_chance(pages, num_frames):
    frames = [-1] * num_frames  
    reference_bit = [0] * num_frames  
    page_faults = 0
    index = 0

    for page in pages:
        found = False
        for i in range(num_frames):
            if frames[i] == page:
                found = True
                reference_bit[i] = 1  
                break
        
        if not found:
            while True:
                if reference_bit[index] == 0:
                    frames[index] = page
                    reference_bit[index] = 0  
                    page_faults += 1
                    index = (index + 1) % num_frames
                    break
                else:
                    reference_bit[index] = 0
                    index = (index + 1) % num_frames
        
        print(f"Pages in memory: {frames}")
    
    print(f"Total page faults: {page_faults}")

pages = [1, 2, 3, 1, 4, 2, 5]
num_frames = 3
second_chance(pages, num_frames)
