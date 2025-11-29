# Exercise 4.2 – Dataset Iterator
# Create list of 5 audio file names. Loop and print each.

song_list = ["Popular", "Sao paulo", "blinding lights", "timeless", "Starboy"]

# for each method
for song in song_list:
    print(f"{song}")

print()
# for in range method
for idx in range(len(song_list)):
    print(f"{idx+1}. {song_list[idx]}")