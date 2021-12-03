# `pydeal_line_length`
A [`pylint`](http://pylint.pycqa.org/en/latest/) to enforce line lengths compatible with ideal monitors.

Although it was designed with [ideal monitor rotation](https://sprocketfox.io/xssfox/2021/12/02/xrandr/) (22 degrees) in mind, the angle is configurable.

Most codebases benefit from being rewritten as Single-Line Applications, but this tool can help if you're working with Big Data or something.

## Installation / Usage

```
pip install pydeal_line_length
```

Run `pylint` with `--load-plugins=pydeal_line_length` to include the checks.

It will raise `W2201: pydeal-line-too-long` or `W2202: pydeal-file-too-long` if the source file will not fit on a reasonable monitor setup.


To run on `pydeal_line_length`'s own code, disabling all other checks:

```
pylint --load-plugins=pydeal_line_length --disable=all --enable=pydeal_line_length pydeal_line_length/
```

## References

- Thanks to [@xssfox](https://github.com/xssfox)'s enlightening [original post](https://sprocketfox.io/xssfox/2021/12/02/xrandr/)
- Thanks to [@ervanalb](https://github.com/ervanalb) for noticing that coding standards need to be updated
- Todo: incorporate a tool like [`max4`](https://github.com/zbanks/four-char-max) for automatically reformatting lines that are too long.
- See also: [`soapystone`](https://github.com/zbanks/soapystone), for ensuring your code meets the standards required for jolly cooperation.

