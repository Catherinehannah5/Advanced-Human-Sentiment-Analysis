import React from "react";
import { mount } from 'enzyme';
import Form from './App';
import Enzyme from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import Form from './App';

Enzyme.configure({adapter: new Adapter() });

describe("<Form />", () => {
  let wrapper;
  const setState = jest.fn();
  const useStateSpy = jest.spyOn(React, "useState")
  useStateSpy.mockImplementation((init) => [init, setState]);

  beforeEach(() => {
      wrapper = Enzyme.mount(Enzyme.shallow(<Form />).get(0))
  });

  afterEach(() => {
      jest.clearAllMocks();
  });

  describe("Keyword Input", () => {
    it("Should capture input correctly onChange", () => {
        const input = wrapper.find("input").at(0);
        input.instance().value = "Test";
        input.simulate("change");
        expect(setState).toHaveBeenCalledWith("Test");
    });
});

it('calls onSubmit prop function when form is submitted', () => {
    const onSubmitFn = jest.fn();
    const wrapper = mount(<Form onSubmit={onSubmitFn}/>);
    const form = wrapper.find('form');
    form.simulate('submit');
    expect(onSubmitFn).toHaveBeenCalledTimes(1);
  });