import subprocess as sp
import json


def probe(ytdl_path):
    if type(ytdl_path) != str:
        raise Exception('Give ffprobe a full file path of the file')

    command = ["ffprobe",
               "-loglevel", "quiet",
               "-print_format", "json",
               "-show_format",
               "-show_streams",
               ytdl_path
               ]

    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT)
    out, err = pipe.communicate()
    return json.loads(out)


def duration(ytdl_path):
    _json = probe(ytdl_path)

    if 'format' in _json:
        if 'duration' in _json['format']:
            return float(_json['format']['duration'])

    if 'streams' in _json:
        for s in _json['streams']:
            if 'duration' in s:
                return float(s['duration'])

    raise Exception('duration Not found')


if __name__ == "__main__":
    print(duration("examplefile.mp4"))