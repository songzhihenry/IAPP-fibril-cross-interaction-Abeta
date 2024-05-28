'''def print_color_codes():
    # Get color indices and names
    color_indices = cmd.get_color_indices()
    with open('color-codes.txt','w') as f:
        # Print color codes
        for name, index in color_indices:
            #print(f"{name}: {index}")
            f.write(f"{name}  {index}\n")

def get_all_resi_codes():
    #pymol.color_list = []
    pymol.color_dict = {}
    #cmd.iterate('all', 'pymol.color_list.append((resi,color))')
    cmd.iterate('all', 'pymol.color_dict[resi]=color')
    print(pymol.color_dict)


def get_resi_name():
    # Create an empty list to store residue colors
    pymol.residue_colors = {}

    # Iterate through all residues
    cmd.iterate('all','pymol.residue_colors[resi]=str(color)')

    # Convert color indices to RGB values
    rgb_values = [cmd.get_color_tuple(color) for resi,color in pymol.residue_colors.items()]

    # Print the RGB values for each residue
    with open('color-codes.txt','w') as f:
        for rgb1,rgb2,rgb3 in rgb_values:
            f.write(f"{rgb1}  {rgb2}  {rgb3}\n")'''

def fib_resi_sele(name, chain_range,resi_id,resi_n):
    '''
    name -- name of your selection
    chain_range -- chain from which to which
    resi_id -- residue id on a chain
    resi_n -- residue number in a chain
    '''
    # Initialize an empty selection
    cmd.select(f'{name}', 'none')
    # Merge each selection iteratively
    if type(chain_range) == int:
        for i in range(chain_range):
            cmd.select(f'sel_resi', f'resi {resi_id + i * resi_n}')
            cmd.select(f'{name}', f'{name} or sel_resi', merge=1)
    if type(chain_range) == tuple:
        for i in range(chain_range[0],chain_range[1]):
            cmd.select(f'sel_resi', f'resi {resi_id + i * resi_n}')
            cmd.select(f'{name}', f'{name} or sel_resi', merge=1)
    cmd.delete('sel_resi')

