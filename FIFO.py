def fifo(pages, num_frames):
    frames = [-1] 
    page_faults = 0
    index = 0

    for page in pages:
        if page not in frames:
            frames[index] = page
            index = (index + 1) % num_frames
            page_faults += 1
        
        print(f"Pages in memory: {frames}")
    
    print(f"Total page faults: {page_faults}")


pages = [1, 2, 3, 1, 4, 2, 5]
num_frames = 3
fifo(pages, num_frames)
