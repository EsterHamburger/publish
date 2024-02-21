
const BasicInput = ({ name, value, onChange }) => {
  return <>
    <label>{name}:
      <input type="text" name={name} value={value} onChange={onChange} />
    </label>
  </>;
};

export default BasicInput;
