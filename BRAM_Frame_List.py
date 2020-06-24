import sys
import os
import json
import patch_mem


def listTiles(mddFile, memoryToPrint, jsonFile):
    with open(jsonFile) as openFile:
        jsonData = json.load(openFile)
    mddData = patch_mem.readAndFilterMDDData(mddFile, memoryToPrint)
    for mdd in mddData:
        assert mdd.tile in jsonData
        entry = jsonData[mdd.tile]["bits"]["BLOCK_RAM"]
        print(
            "Tile: {},\tFrame Address: {},\t# of Frames: {:4d},\tWord Offset: {:3d},\t# of Words: {:4d}"
            .format(
                mdd.tile, entry["baseaddr"], entry["frames"], entry["offset"],
                entry["words"]
            )
        )


if __name__ == "__main__":
    assert len(sys.argv) == 4, \
        "Usage: mddFile memoryToPrint jsonFile"
    listTiles(sys.argv[1], sys.argv[2], sys.argv[3])