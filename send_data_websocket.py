import asyncio
import time

async def sendData(sequence_green_time: dict, send_signal_to_clients, cycle_time, cap1, cap2, cap3, cap4, yellow_time=5):
    from getTimings import getTimings
    from setSequence import setSequence
    
    current_timestamp = 0
    index_map = {signal: i for i, signal in enumerate(sequence_green_time)}

    while True:  # Infinite loop to continuously cycle through signals
        # Get new timings based on current timestamp
        new_timings = getTimings(cycle_time, cap1, cap2, cap3, cap4, current_timestamp)
        
        if new_timings is None:
            # If we can't get timings (e.g., end of video), break the loop
            break
            
        # Update sequence based on new vehicle counts
        sequence_green_time = setSequence(new_timings)
        
        # Update index map for the new sequence
        index_map = {signal: i for i, signal in enumerate(sequence_green_time)}
        
        for i in range(1, 5):
            green_time = max(sequence_green_time[i] - yellow_time, 5)  # Minimum 5 seconds green

            # Green state
            start = time.time()
            while (time.time() - start) < green_time:
                signal = ["red"] * 4
                signal[index_map[i]] = "green"
                await send_signal_to_clients(signal)
                await asyncio.sleep(1)

            # Yellow state
            start = time.time()
            while (time.time() - start) < yellow_time:
                signal = ["red"] * 4
                signal[index_map[i]] = "yellow"
                await send_signal_to_clients(signal)
                await asyncio.sleep(1)
        
        # Move to next timestamp (current time + cycle time)
        current_timestamp += cycle_time
        print(f"Completed cycle, moving to timestamp: {current_timestamp} seconds")