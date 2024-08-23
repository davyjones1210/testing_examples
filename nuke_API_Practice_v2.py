def get_Input_Seq():
    # function to get background information and resolution
    bg_info = nuke.choice("Choice", "Checker Board or Color Wheel?\n", ("0: Checker Board", "1: Color Wheel"),
                          default=0)
    print(bg_info)

    bg_res = nuke.choice("Choice", "Please select the resolution of the sequence you want to create\n",
                         ["0: 1920x1080", "1: 2048x1152", "2: 3840x2160", "3: 4096x2160"], default=0)
    print(bg_res)

    return bg_info, bg_res

def get_Output_Loc():
    file_name = nuke.getFilename("Please enter the file name you would like to write this sequence to ", default='C:/Nuke_API_Practice/Kunal_Test_HD_to_HD_h264_MOV_FILE.mov')
    print(file_name)

    return file_name

def get_file_path():
    # function to get file path to where you would like to create the sequence
    file_name = nuke.getFilename("Please enter the file name using VFX naming format", default='C:/Nuke_API_Practice/kunal_test_seq.####.exr')
    print(file_name)

    return file_name


# def check_input(bg_info, bg_res):
#     #function to check if given input is correct or not
#     if bg_info is None or bg_res is None:
#         nuke.message("Please select a choice and click 'OK'")
#         return 0
#
#     else:
#         return 1


def clear_all_nodes():
    for node in nuke.allNodes():
        nuke.delete(node)


def write_sequence(bg_type, bg_resol, full_file_path):
    # Start by manually writing out a 10 frame HD (1920x1080) sequence of a checker board or color wheel.
    # Use a vfx naming format like kunal_test_seq.####.exr

    checker_board2 = nuke.createNode(bg_type, inpanel=False)
    checker_board2.knob('format').setValue(bg_resol)

    write_node1 = nuke.createNode('Write', inpanel=False)
    write_node1.setInput(0, checker_board2)

    viewer_node = nuke.createNode('Viewer')
    viewer_node.setInput(0, checker_board2)

    write_node1.knob('file').setValue(str(full_file_path))

    write_node1.knob('create_directories').setValue(True)
    write_node1.knob('use_limit').setValue(True)

    write_node1.knob('last').setValue(10)
    ranges = nuke.FrameRanges('1-10')
    nuke.render(write_node1, ranges)


# for node in nuke.allNodes():
#    nuke.delete(node)

def read_seq_write_mov(full_file_path, saved_file_path):
    # Reads in the image sequence
    read_node1 = nuke.createNode('Read', inpanel=False)
    read_node1.setXYpos(read_node1.xpos() + 200, read_node1.ypos())
    read_node1.knob('file').setValue(str(full_file_path))
    read_node1.knob('updateLocalization').execute()

    # Letter box to 2.34 aspect (820 height for HD - black bars across top/bottom 130 pixels)

    crop_node1 = nuke.createNode('Crop')
    crop_node1.knob('preset').setValue(7)
    crop_node1.knob('crop').setValue(True)
    crop_node1.knob('reset').execute()
    crop_node1.setInput(0, read_node1)

    reformat_node2 = nuke.createNode('Reformat', inpanel=False)
    reformat_node2.knob('black_outside').setValue(True)
    reformat_node2.setInput(0, crop_node1)

    # Add frame counter to the bottom left of the letterboxed portion of the frame.
    # This should show the current frame in the viewer.

    text_node1 = nuke.createNode('Text', inpanel=False)
    text_node1.knob('message').setValue("frame [frame]")
    text_node1.knob('scale').setValue(2)
    text_node1.knob('xjustify').setValue(0)
    text_node1.knob('yjustify').setValue(3)
    text_node1.setInput(0, reformat_node2)

    # Add your vfx studio KVFX​​ to the top right.
    text_node2 = nuke.createNode('Text', inpanel=False)
    text_node2.knob('message').setValue("KVFX")
    text_node2.knob('scale').setValue(2)
    text_node2.knob('xjustify').setValue(2)
    text_node2.knob('yjustify').setValue(1)
    text_node2.setInput(0, text_node1)

    # Write the sequence out as an HD h264 encoded mov.

    write_node2 = nuke.createNode('Write', inpanel=False)
    write_node2.knob('file').setValue(str(saved_file_path))
    write_node2.knob('create_directories').setValue(True)
    write_node2.knob('use_limit').setValue(True)
    write_node2.knob('colorspace').setValue("mov")
    write_node2.knob('file_type').setValue("mov")
    write_node2.knob('mov64_codec').setValue(14)
    write_node2.knob('last').setValue(10)
    write_node2.setInput(0, text_node2)
    ranges = nuke.FrameRanges('1-10')

    viewer_node2 = nuke.createNode('Viewer')
    viewer_node2.setInput(0, text_node2)

    nuke.render(write_node2, ranges)


# start of program
# Clearing all previous nodes
clear_all_nodes()

# calling the function to get background info and background resolution

(background_info, background_resolution) = get_Input_Seq()

if background_info == 0:
    bg_type = 'CheckerBoard2'

elif background_info == 1:
    bg_type = 'ColorWheel'

if background_resolution == 0:
    bg_resol = "FullHD"

elif background_resolution == 1:
    bg_resol = "2K"

elif background_resolution == 2:
    bg_resol = "UHD_4K"

elif background_resolution == 3:
    bg_resol = "4K_DCP"

full_file_path = get_file_path()


write_sequence(bg_type, bg_resol, full_file_path)

saved_file_path = get_Output_Loc()

read_seq_write_mov(full_file_path, saved_file_path)

