import glob, os


def main(path):
    multiFile2aVariable(path)
    copyMultiFile2aFile(path)


def copyMultiFile2aFile(path):
    os.chdir(path + "/image")
    _data_ = '#include "Arduino.h"\n\n\n'
    filenames = []
    for file in glob.glob("*.xbm"):
        filenames.append(file)
    filenames.sort()
    # print(filenames)
    for filename in filenames:
        f = open(filename, "r")
        data = f.read()
        data = data.replace("static char", "const char")
        data = data.replace("=", "PROGMEM = ")
        _data_ += data
        _data_ += "\n\n"
    f = open(path + "/copyMultiFile2aFile.h", "a+")
    f.write(_data_)
    f.close()


def multiFile2aVariable(path):
    os.chdir(path + "/image")
    size = 0
    _data_file_ = ""
    filenames = []
    for file in glob.glob("*.xbm"):
        filenames.append(file)

    filenames.sort()

    for filename in filenames:
        f = open(filename, "r")
        data = f.read()
        a, b = str(data).split("=")
        c = b.replace(";", "")
        _data_file_ += c + ",\n"
        size = c.count("0x")

    datafile = '#include "Arduino.h"\n\n\n'
    datafile += "#define image_width 32\n"
    datafile += "#define image_height 32\n\n\n"
    datafile += "const char image_bit[][" + str(size) + "] PROGMEM = {\n"
    datafile += _data_file_
    datafile += "};"
    f = open(path + "/multiFile2aVariable.h", "w")
    f.write(datafile)
    f.close()


if __name__ == "__main__":
    main(os.getcwd())

