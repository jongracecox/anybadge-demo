from anybadge import Badge, version
from flask import Flask

thresholds={
  2: 'red',
  4: 'orange',
  8: 'yellow',
  10: 'green'
}

badges = [

  # Basic badge
  Badge('anybadge', value=version),

  # Badge with padding
  Badge('anybadge', value=version, num_padding_chars=0),

  # Badge with value suffix
  Badge('coverage', value='98.67', value_suffix='%'),
  
  # Some examples to demonstrate threshold dictionaries.
  # The thresolds from these examples are defined above.
  Badge('threshold', value=1, thresholds=thresholds),
  Badge('threshold', value=2, thresholds=thresholds),
  Badge('threshold', value=3, thresholds=thresholds),
  Badge('threshold', value=9, thresholds=thresholds),
  Badge('threshold', value=10, thresholds=thresholds),

  # Two threshold examples showing what happens when
  # the value exceeds the max defined in the threshold
  # dict, and how that is affected by the
  # use_max_when_value_exceeds attribute.
  Badge('threshold', value=11, thresholds=thresholds,
        default_color='red'),
  Badge('threshold', value=11, thresholds=thresholds,
        default_color='red', 
        use_max_when_value_exceeds=False),
  Badge('float_num', 12.345, default_color='teal', num_padding_chars=1),
  Badge('float_str', "12.345", default_color='teal', num_padding_chars=1),
  Badge('no padding', 123),
  Badge('label padding', 123, num_label_padding_chars=2),
  Badge('value padding', 123, num_value_padding_chars=2),
]

app = Flask(__name__, static_folder='.')

@app.route('/')
def root():
    return '<br>'.join(['<pre>' + repr(b) + '</pre>' + 
    str(b) for b in badges])

app.run(host='0.0.0.0', port='3000')